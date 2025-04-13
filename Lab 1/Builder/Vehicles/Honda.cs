namespace Builder.Instances.Vehicles;

public class Honda : IVehicle
{
    public double Weight { get; set; } = 1400;
    public double Length { get; set; } = 4.3;
    public double MaxSpeed { get; set; } = 220;
    public EWheelDriveType WheelDriveType { get; set; } = EWheelDriveType.Front;
    public EVehicleClass VehicleClass { get; set; } = EVehicleClass.Hatchback;
    public EColor Color { get; set; } = EColor.Green;
}