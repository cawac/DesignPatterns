namespace Builder;

public class Cargo : ICar
{
    public string Name { get; set; }
    public double Weight { get; set; }
    public double Length { get; set; }
    public double MaxSpeed { get; set; }
    public double Tonnage { get; set; }
    public double TankVolume { get; set; }
    public int AxlesAmount { get; set; }
}