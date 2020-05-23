// https://codeforces.com/contest/1347/problem/D

import java.io.*
import kotlin.math.max

private var br: BufferedReader? = null

private fun br(): BufferedReader? {
    if (br == null) {
        var isLocal = false
        val file = File("./file/input.txt")

        try {
            isLocal = file.exists()
        } catch (e: Exception) {

        }

        br = if (isLocal) {
            BufferedReader(BufferedReader(FileReader(file)));
        } else {
            BufferedReader(InputStreamReader(System.`in`))
        }
    }
    return br
}

private fun readLn() = br()?.readLine()!! // string line
private fun readInt() = readLn().toInt() // single int
private fun readLong() = readLn().toLong() // single long
private fun readDouble() = readLn().toDouble() // single double
private fun readStrings() = readLn().split(" ") // list of strings
private fun readInts() = readStrings().map { it.toInt() } // list of ints
private fun readLongs() = readStrings().map { it.toLong() } // list of longs
private fun readDoubles() = readStrings().map { it.toDouble() } // list of doubles
private fun readArray() = readStrings().map { it.toInt() }.toIntArray() // list of ints

fun case() {
    val n = readInt()
    var a = readArray()

    var left = 0
    var right = n - 1
    var step = 0
    var last = 0
    var leftsum = 0
    var rightsum = 0
    while (left <= right) {
        var current = 0
        while (left <= right) {
            if (current > last) {
                break
            }

            current += a[left]
            leftsum += a[left]
            left += 1
        }
        last = current
        if (current > 0) {
            step += 1
        }

        current = 0
        while (left <= right) {
            if (current > last) {
                break
            }

            current += a[right]
            rightsum += a[right]
            right -= 1
        }
        last = current
        if (current > 0) {
            step += 1
        }
    }

    println("${step} ${leftsum} ${rightsum}")
}

fun main() {
    var t = readInt()
    while (t-- > 0) {
        case()
    }
}