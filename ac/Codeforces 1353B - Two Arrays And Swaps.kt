// https://codeforces.com/contest/1353/problem/B

import java.io.*

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
    var a = readInts().toMutableList()
    var b = readInts().toMutableList()

    a = a.sorted().toMutableList()
    b = b.sortedDescending().toMutableList()

    while (k-- > 0) {
        if (b[0] > a[0]) {
            a[0] = b[0].also { b[0] = a[0] }
            a = a.sorted().toMutableList()
            b = b.sortedDescending().toMutableList()
        } else {
            break
        }
    }

    println(a.sum())
}

fun main() {
    var t = readInt()
    while (t-- > 0) {
        case()
    }
}