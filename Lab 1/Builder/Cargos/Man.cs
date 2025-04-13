namespace Builder.Instances;

public class Man : ICargo
{
    public double Weight { get; set; } = 11500;
    public double Length { get; set; } = 10.2;
    public double MaxSpeed { get; set; } = 105;
    public double Tonnage { get; set; } = 18000;
    public double TankVolume { get; set; } = 580;
    public int AxlesAmount { get; set; } = 4;
}