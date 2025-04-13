namespace Builder.Instances.Tanks;

public class Abrams : ITank
{
    public double Weight { get; set; } = 62000;
    public double Length { get; set; } = 9.7;
    public double MaxSpeed { get; set; } = 67;
    public double ProjectileCaliber { get; set; } = 120;
    public int ShotsPerMinute { get; set; } = 12;
    public int CrewSize { get; set; } = 3;
}