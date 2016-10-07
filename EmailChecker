using System;
using System.Text.RegularExpressions;
class Solution
{

    static void Main(String[] args)
    {
        Console.WriteLine("Input in your email:");
        string s = Console.ReadLine();
        Regex email = new Regex(@"^[A-Za-z0-9]+@[A-Za-z0-9]+\.[a-z]+$");
        Console.WriteLine(email.IsMatch(s) ? "Valid email address" : "Invalid email address");
    }
}
