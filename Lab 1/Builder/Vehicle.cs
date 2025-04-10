namespace Builder;

public enum EColor
{
    None = 0,
    Red = 1,
    Blue = 2,
    Green = 3,
    Orange = 4,
}

public enum EWheelDriveType
{
    None = 0,
    Front = 1,
    Back = 2,
    All = 3
}

public enum EVehicleClass
{
    None = 0,
    Hatchback = 1,
    Sedan = 2,
    Coupe = 4,
}

public class Vehicle : ICar
{
    public EWheelDriveType WheelDriveType { get; set; }

    public EVehicleClass VehicleClass { get; set; }

    public EColor Color { get; set; }
    public double Weight { get; set; }
    public double Length { get; set; }
    public double MaxSpeed { get; set; }
    public List<string> Features { get; set; }
}

public class Audi : Vehicle
{
    public Audi()
    {
        this.Weight = 1500;
        this.Length = 4.5;
        this.MaxSpeed = 240;
        this.WheelDriveType = EWheelDriveType.All;
        this.VehicleClass = EVehicleClass.Sedan;
        this.Color = EColor.Red;
    }
}

public class Honda : Vehicle
{
    public Honda()
    {
        this.Weight = 1400;
        this.Length = 4.3;
        this.MaxSpeed = 220;
        this.WheelDriveType = EWheelDriveType.Front;
        this.VehicleClass = EVehicleClass.Hatchback;
        this.Color = EColor.Green;
    }

}

public class Tesla : Vehicle
{
    public Tesla()
    {
        this.Weight = 1800;
        this.Length = 4.7;
        this.MaxSpeed = 250;
        this.WheelDriveType = EWheelDriveType.All;
        this.VehicleClass = EVehicleClass.Coupe;
        this.Color = EColor.Blue;
    }
}
