var a, b, ans: longint;
begin
readln(a, b);
ans := b - 1;
while ans mod a <> 1 do
    ans := ans + b;
writeln(ans)
end.
