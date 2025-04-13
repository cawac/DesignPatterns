namespace Builder.Instances.Tanks;

public class Tiger : ITank
{
    public double Weight { get; set; } = 57000;
    public double Length { get; set; } = 8.45;
    public double MaxSpeed { get; set; } = 38;
    public double ProjectileCaliber { get; set; } = 88;
    public int ShotsPerMinute { get; set; } = 5;
    public int CrewSize { get; set; } = 5;
}
