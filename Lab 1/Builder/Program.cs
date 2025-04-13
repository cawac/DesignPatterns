

using Builder;

public static class Program
{
    public static void Main()
    {
        TankBuilder tankBuilder = new TankBuilder();
        tankBuilder.Build(3, 120, 12);
        var tank = tankBuilder.GetResult();
        tankBuilder.Reset();
    }
}