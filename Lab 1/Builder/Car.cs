namespace Builder;

public interface ICar
{
    public double Weight { get; set; }
    public double Length { get; set; }
    public double MaxSpeed { get; set; }
    public List<string> Features { get; set; }
}