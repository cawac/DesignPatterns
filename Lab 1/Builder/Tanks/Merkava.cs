namespace Builder.Instances.Tanks;

public class Merkava : ITank
{
    public double Weight { get; set; } = 65000;
    public double Length { get; set; } = 9.04;
    public double MaxSpeed { get; set; } = 64;
    public double ProjectileCaliber { get; set; } = 120;
    public int ShotsPerMinute { get; set; } = 7;
    public int CrewSize { get; set; } = 4;
}