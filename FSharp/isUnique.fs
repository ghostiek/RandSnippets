let isUnique(s:seq<'a>) = if (s |> Seq.distinct |> Seq.length = (s |> Seq.length)) then true else false
