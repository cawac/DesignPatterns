namespace Builder;

public class Cargo : ICar
{
    public double Tonnage { get; set; }
    public double TankVolume { get; set; }
    public int AxlesAmount { get; set; }
    public double Weight { get; set; }
    public double Length { get; set; }
    public double MaxSpeed { get; set; }
    public List<string> Features { get; set; }
}

public class Volvo : Cargo
{
    public Volvo()
    {
        this.Weight = 12000;
        this.Length = 10.5;
        this.MaxSpeed = 110;
        this.Tonnage = 20000;
        this.TankVolume = 600;
        this.AxlesAmount = 3;
    }
}

public class Man : Cargo
{
    public Man()
    {
        this.Weight = 11500;
        this.Length = 10.2;
        this.MaxSpeed = 105;
        this.Tonnage = 18000;
        this.TankVolume = 580;
        this.AxlesAmount = 2;
    }
}

public class Scania : Cargo
{
    public Scania()
    {
        this.Weight = 12500;
        this.Length = 11.0;
        this.MaxSpeed = 115;
        this.Tonnage = 22000;
        this.TankVolume = 650;
        this.AxlesAmount = 3;
    }
}

