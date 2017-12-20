//Shifts a seq one one cell to the right
let RightShift(s:seq<'a>) =
    let mutable placeholder = s |> Array.ofSeq
    for i in 0..((s |> Seq.length) - 1) do
        placeholder.[(i+1)% placeholder.Length] <- s |> Seq.item i
    placeholder
