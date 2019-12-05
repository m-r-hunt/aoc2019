open System
open D1

[<EntryPoint>]
let main argv =
    let d1result = d1 ()
    printfn "Day 1: %d, %d" (fst d1result) (snd d1result)
    0 // return an integer exit code
