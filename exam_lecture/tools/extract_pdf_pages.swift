#!/usr/bin/env swift

import Foundation
import PDFKit

struct LayoutLine: Codable {
    let text: String
    let x: Double
    let y: Double
    let width: Double
    let height: Double
    let dominantFontSize: Double
}

guard CommandLine.arguments.count == 5 else {
    fputs(
        "Usage: extract_pdf_pages.swift <input.pdf> <output-directory> <start-page> <end-page>\n",
        stderr
    )
    exit(2)
}

let inputURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2], isDirectory: true)

guard
    let startPage = Int(CommandLine.arguments[3]),
    let endPage = Int(CommandLine.arguments[4]),
    startPage >= 1,
    endPage >= startPage
else {
    fputs("Page numbers must define a positive, inclusive range.\n", stderr)
    exit(2)
}

guard let document = PDFDocument(url: inputURL) else {
    fputs("Unable to open PDF: \(inputURL.path)\n", stderr)
    exit(1)
}

guard endPage <= document.pageCount else {
    fputs(
        "Requested page \(endPage), but the document has \(document.pageCount) pages.\n",
        stderr
    )
    exit(2)
}

try FileManager.default.createDirectory(
    at: outputURL,
    withIntermediateDirectories: true
)

for pageNumber in startPage...endPage {
    guard let page = document.page(at: pageNumber - 1) else {
        fputs("Unable to read page \(pageNumber).\n", stderr)
        exit(1)
    }

    let pageText = page.string ?? ""
    let outputText = "===== PDF PAGE \(pageNumber) =====\n\(pageText)\n"
    let outputFile = outputURL.appendingPathComponent(
        String(format: "page-%04d.txt", pageNumber)
    )
    try outputText.write(to: outputFile, atomically: true, encoding: .utf8)

    let mediaBox = page.bounds(for: .mediaBox)
    let fullPageSelection = page.selection(for: mediaBox)
    let pageAttributedString = page.attributedString
    let layoutLines = (fullPageSelection?.selectionsByLine() ?? []).compactMap {
        selection -> LayoutLine? in
        guard let text = selection.string?.trimmingCharacters(in: .newlines),
              !text.isEmpty
        else {
            return nil
        }

        let bounds = selection.bounds(for: page)
        var fontWeights: [Double: Int] = [:]
        if let attributed = pageAttributedString {
            for rangeIndex in 0..<selection.numberOfTextRanges(on: page) {
                let range = selection.range(at: rangeIndex, on: page)
                guard range.location != NSNotFound,
                      NSMaxRange(range) <= attributed.length
                else {
                    continue
                }
                attributed.enumerateAttribute(.font, in: range) {
                    value, fontRange, _ in
                    guard let font = value as? NSFont else { return }
                    let roundedSize =
                        (Double(font.pointSize) * 10).rounded() / 10
                    fontWeights[roundedSize, default: 0] += fontRange.length
                }
            }
        }
        let dominantFontSize = fontWeights.max { left, right in
            left.value < right.value
        }?.key ?? Double(bounds.height)

        return LayoutLine(
            text: text,
            x: Double(bounds.minX),
            y: Double(bounds.minY),
            width: Double(bounds.width),
            height: Double(bounds.height),
            dominantFontSize: dominantFontSize
        )
    }
    let layoutData = try JSONEncoder().encode(layoutLines)
    let layoutFile = outputURL.appendingPathComponent(
        String(format: "page-%04d.layout.json", pageNumber)
    )
    try layoutData.write(to: layoutFile, options: .atomic)
}

print(
    "Extracted pages \(startPage)–\(endPage) from \(document.pageCount)-page PDF " +
    "to \(outputURL.path)"
)
