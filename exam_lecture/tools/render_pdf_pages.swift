#!/usr/bin/env swift

import AppKit
import Foundation
import PDFKit

guard CommandLine.arguments.count == 3 else {
    fputs("Usage: render_pdf_pages.swift <input.pdf> <output-directory>\n", stderr)
    exit(2)
}

let inputURL = URL(fileURLWithPath: CommandLine.arguments[1])
let outputURL = URL(fileURLWithPath: CommandLine.arguments[2], isDirectory: true)

guard let document = PDFDocument(url: inputURL) else {
    fputs("Unable to open PDF: \(inputURL.path)\n", stderr)
    exit(1)
}

try FileManager.default.createDirectory(
    at: outputURL,
    withIntermediateDirectories: true
)

let scale: CGFloat = 1.6

for pageIndex in 0..<document.pageCount {
    guard let page = document.page(at: pageIndex) else { continue }
    let bounds = page.bounds(for: .mediaBox)
    let pixelWidth = Int(bounds.width * scale)
    let pixelHeight = Int(bounds.height * scale)

    guard let context = CGContext(
        data: nil,
        width: pixelWidth,
        height: pixelHeight,
        bitsPerComponent: 8,
        bytesPerRow: 0,
        space: CGColorSpaceCreateDeviceRGB(),
        bitmapInfo: CGImageAlphaInfo.premultipliedLast.rawValue
    ) else {
        fputs("Unable to create image context for page \(pageIndex + 1)\n", stderr)
        exit(1)
    }

    context.setFillColor(NSColor.white.cgColor)
    context.fill(CGRect(x: 0, y: 0, width: pixelWidth, height: pixelHeight))
    context.scaleBy(x: scale, y: scale)
    page.draw(with: .mediaBox, to: context)

    guard let image = context.makeImage() else {
        fputs("Unable to render page \(pageIndex + 1)\n", stderr)
        exit(1)
    }
    let bitmap = NSBitmapImageRep(cgImage: image)
    guard let data = bitmap.representation(using: .png, properties: [:]) else {
        fputs("Unable to encode page \(pageIndex + 1)\n", stderr)
        exit(1)
    }

    let outputFile = outputURL.appendingPathComponent(
        String(format: "page-%02d.png", pageIndex + 1)
    )
    try data.write(to: outputFile)
}

print("Rendered \(document.pageCount) pages to \(outputURL.path)")
