// https://codeforces.com/contest/1347/problem/E

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

    if (n < 4) {
        println(-1)
        return
    }

    var result = mutableListOf(2, 4, 1, 3)
    for (i in 5..n step 2) {
        result.add(i)
    }
    result.reverse()
    for (i in 6..n step 2) {
        result.add(i)
    }

    var isFirst = true
    for (element in result) {
        if (isFirst) {
            isFirst = false
        } else {
            print(" ")
        }
        print(element)
    }
    println()
}

fun main() {
    var t = readInt()
    while (t-- > 0) {
        case()
    }
}