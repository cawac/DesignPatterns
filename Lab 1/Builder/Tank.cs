namespace Builder;

public class Tank: ICar
{
    public double ProjectileCaliber { get; set; }
    public int ShotsPerMinute { get; set; }
    public int CrewSize { get; set; }
    public double Weight { get; set; }
    public double Length { get; set; }
    public double MaxSpeed { get; set; }
    public List<string> Features { get; set; }
}

public class Abrams : Tank
{
    public Abrams()
    {
        this.Weight = 62000;
        this.Length = 9.7;
        this.MaxSpeed = 67;
        this.ProjectileCaliber = 120;
        this.ShotsPerMinute = 6;
        this.CrewSize = 4;
    }
}

public class Merkava : Tank
{
    public Merkava()
    {
        this.Weight = 65000;
        this.Length = 9.04;
        this.MaxSpeed = 64;
        this.ProjectileCaliber = 120;
        this.ShotsPerMinute = 7;
        this.CrewSize = 4;
    }
}

public class Tiger : Tank
{
    public Tiger()
    {
        this.Weight = 57000;
        this.Length = 8.45;
        this.MaxSpeed = 38;
        this.ProjectileCaliber = 88;
        this.ShotsPerMinute = 5;
        this.CrewSize = 5;
    }
}

