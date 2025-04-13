namespace Builder;

public interface ICargo : ICar
{
    public double Tonnage { get; set; }
    public double TankVolume { get; set; }
    public int AxlesAmount { get; set; }
}