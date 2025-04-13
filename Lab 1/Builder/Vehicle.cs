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
    public string Name { get; set; }
    public double Weight { get; set; }
    public double Length { get; set; }
    public double MaxSpeed { get; set; }
    public EWheelDriveType WheelDriveType { get; set; }
    public EVehicleClass VehicleClass { get; set; }
    public EColor Color { get; set; }
}