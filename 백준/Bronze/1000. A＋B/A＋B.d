import std.stdio;
import std.conv;
import std.string;
 
void main() {
    string[] r;
    try
        r = readln().split();
    catch (StdioException e)
        r = ["0", "0"];
    auto a = to!int(r[0]);
    auto b = to!int(r[1]);
    auto ans = a + b;
    writeln(ans);
}