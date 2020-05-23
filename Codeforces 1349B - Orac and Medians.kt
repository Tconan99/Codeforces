// https://codeforces.com/problemset/problem/1349/B

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
    var (n, k) = readInts()
    var s = readArray()

    if (n == 1 && s[0] == k) {
        println("yes")
        return
    }

    for (i in 0..n-1) {
        if (s[i] == k) {
            if (i > 0) {
                if (s[i - 1] >= s[i]) {
                    println("yes")
                    return
                }
            }

            if (i < n - 1) {
                if (s[i + 1] >= s[i]) {
                    println("yes")
                    return
                }
            }
        }
    }
    println("no")
}

fun main() {
    var t = readInt()
    while (t-- > 0) {
        case()
    }
}