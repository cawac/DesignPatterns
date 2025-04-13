namespace Builder.Instances;

public class Volvo: ICargo
{
    public double Weight { get; set; } = 12000;
    public double Length { get; set; } = 10.5;
    public double MaxSpeed { get; set; } = 110;
    public double Tonnage { get; set; } = 20000;
    public double TankVolume { get; set; } = 600;
    public int AxlesAmount { get; set; } = 5;
}