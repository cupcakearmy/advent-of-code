---
to: <%= dir %>/typescript/main.ts
unless_exists: true
---
import fs from 'node:fs'
import path from 'node:path'

// SETUP
const INPUT = fs.readFileSync(path.join(import.meta.dir, '../input.txt'), 'utf-8').trim()
const TEST = fs.readFileSync(path.join(import.meta.dir, '../test.txt'), 'utf-8').trim()

// TASK

function partA(input: string) {}

function partB(input: string) {}

console.log('Part A:')
partA(TEST)
partA(INPUT)

console.log('Part B:')
partA(TEST)
partB(INPUT)
