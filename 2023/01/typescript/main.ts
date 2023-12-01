import fs from 'node:fs'
import path from 'node:path'

// SETUP
const INPUT = fs.readFileSync(path.join(import.meta.dir, '../input.txt'), 'utf-8').trim()
const TEST = fs.readFileSync(path.join(import.meta.dir, '../test.txt'), 'utf-8').trim()

// TASK

function partA(input: string) {
  const total = input
    .split('\n')
    .map((line) => {
      const digits = line.split('').filter((c) => /\d/.test(c))
      return parseInt(digits[0]! + digits[digits.length - 1])
    })
    .reduce((acc, cur) => acc + cur, 0)
  console.log(total)
}

function partB(input: string) {
  const names = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
  const total = input
    .split('\n')
    .map((line) => {
      let first = 0
      let last = 0
      root: for (let i = 0; i < line.length; i++) {
        for (const [num, name] of names.entries()) {
          const asString = (num + 1).toString()
          if (line[i] === asString || line.slice(i).startsWith(name)) {
            first = num + 1
            break root
          }
        }
      }

      root: for (let i = line.length; i >= 0; i--) {
        for (const [num, name] of names.entries()) {
          const asString = (num + 1).toString()
          if (line[i] === asString || line.slice(i).startsWith(name)) {
            last = num + 1
            break root
          }
        }
      }

      return last + 10 * first
    })
    .reduce((acc, cur) => acc + cur, 0)
  console.log(total)
}

console.log('Part A:')
partA(TEST)
partA(INPUT)

console.log('Part B:')
partB(TEST)
partB(INPUT)
