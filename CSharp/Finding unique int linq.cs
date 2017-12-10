using System;
using System.Linq;
using System.Collections.Generic;
using System.IO;
class Solution
{
//https://www.hackerrank.com/challenges/lonely-integer
    static void Main(String[] args)
    {
        int _a_size = Convert.ToInt32(Console.ReadLine());
        String[] arr = Console.ReadLine().Split(' ');
        int[] myInts = Array.ConvertAll(arr, s => int.Parse(s));
        var num = myInts.GroupBy(i => i).Where(g => g.Count() == 1).Select(g => g.Key).FirstOrDefault();
        Console.WriteLine(num);
    }
}
