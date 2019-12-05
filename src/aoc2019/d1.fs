module D1

open System

let readLines filePath = System.IO.File.ReadLines filePath

let fuelCost m = m / 3 - 2

let rec iteratedFuelCost m =
    if fuelCost m <= 0 then
        0
    else
        fuelCost m + iteratedFuelCost (fuelCost m)

let d1 () =
    let input =
        readLines "d1input.txt"
        |> Seq.map int
    let part1 =
        input
        |> Seq.map fuelCost
        |> Seq.sum
    let part2 =
        input
        |> Seq.map iteratedFuelCost
        |> Seq.sum
    (part1, part2)
