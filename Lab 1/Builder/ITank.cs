namespace Builder;

public interface ITank: ICar
{
    public double ProjectileCaliber { get; set; }
    public int ShotsPerMinute { get; set; }
    public int CrewSize { get; set; }
}