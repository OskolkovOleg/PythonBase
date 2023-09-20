var a, b, ans: longint;
begin
readln(a, b);
ans := 1;
while ans mod b <> b - 1 do
    ans := a + ans;
writeln(ans)
end.
