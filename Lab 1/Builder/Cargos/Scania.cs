namespace Builder.Instances;

public class Scania : ICargo
{
    public double Weight { get; set; } = 12500;
    public double Length { get; set; } = 11.0;
    public double MaxSpeed { get; set; } = 115;
    public double Tonnage { get; set; } = 22000;
    public double TankVolume { get; set; } = 650;
    public int AxlesAmount { get; set; } = 3;
}
