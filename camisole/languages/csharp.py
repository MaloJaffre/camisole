from camisole.models import Lang


class CSharp(Lang, name="C#"):
    source_ext = '.cs'
    compiler = '/usr/bin/mcs'
    compile_opts = ['-optimize+']
    interpreter = '/usr/bin/mono'
    reference_source = r'''
using System;
class Program
{
    public static void Main()
    {
        Console.WriteLine(42);
    }
}
'''

    def compile_opt_out(self, output):
        return ['-out:' + output]
