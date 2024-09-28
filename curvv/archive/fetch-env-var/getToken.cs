using System;

class Program
{
    static void Main()
    {
        string value = Environment.GetEnvironmentVariable("keyToAll");

        if (!string.IsNullOrEmpty(value))
        {
            Console.WriteLine($"The value of 'keyToAll' is: {value}");
        }
        else
        {
            Console.WriteLine("The environment variable 'keyToAll' is not set.");
        }
    }
}
