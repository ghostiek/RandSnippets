using System;
using System.Linq;

class Solution
{
  public static void FizzBuzz()
    {
        Enumerable.Range(1, 100)
            .Select(i =>
                (i % 15 == 0) ? "FizzBuzz" :
                (i % 3 == 0) ? "Fizz" :
                (i % 5 == 0) ? "Buzz" :
                i.ToString())
            .ToList()
            .ForEach(x => Console.WriteLine(x));
    }
}
