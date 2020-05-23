// https://codeforces.com/contest/1347/problem/C

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
    var n = readInt()
    var isFirst = true

    var pos = 1;
    var number = 0
    var result = ""
    while (n > 0) {
        val bit = n % 10
        if (bit > 0) {
            number += 1
            if (isFirst) {
                isFirst = false
            } else {
                result += " "
            }
            result += bit * pos
        }

        pos *= 10
        n /= 10
    }
    println(number)
    println(result)
}

fun main() {
    var t = readInt()
    while (t-- > 0) {
        case()
    }
}