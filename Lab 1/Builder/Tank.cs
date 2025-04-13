namespace Builder;

public class Tank: ICar
{
    public string Name { get; set; }
    public double Weight { get; set; }
    public double Length { get; set; }
    public double MaxSpeed { get; set; }
    public double ProjectileCaliber { get; set; }
    public int ShotsPerMinute { get; set; }
    public int CrewSize { get; set; }
}