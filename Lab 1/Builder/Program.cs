

using Builder;

public static class Program
{
    public static void Main()
    {
        TankBuilder tankBuilder = new TankBuilder();
        tankBuilder.BuildBase("Abrams", 120, 12, 40);
        tankBuilder.BuildSpecific(120, 10, 3);
        var tank = tankBuilder.GetResult();
        tankBuilder.Reset();
    }
}