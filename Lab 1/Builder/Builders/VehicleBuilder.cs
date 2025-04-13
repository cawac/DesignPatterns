using Builder.Instances.Vehicles;

namespace Builder;

public class VehicleBuilder: IBuilder<IVehicle>
{
    protected IVehicle? Car { get; set; }
    
    public void Build(EColor Color, EVehicleClass VehicleClass, EWheelDriveType WheelDriveType)
    {
        if (WheelDriveType == EWheelDriveType.Front)
        {
            this.Car = new Honda();
        }
        else if (WheelDriveType == EWheelDriveType.All)
        {
            this.Car = new Audi();
        }
        else
        {
            this.Car = new Tesla();
        }
    }
    
    public IVehicle? GetResult()
    {
        return Car;
    }

    public void Reset()
    {
        return;
    }
}