namespace Builder;

public class VehicleBuilder: IBuilder<Vehicle>
{
    public Vehicle Car { get; set; }

    public void BuildBasePart()
    {
        this.Car.Features.Add("add seats");
        this.Car.Features.Add("add wheels");
    }

    public void BuildAdditionPart()
    {
        this.Car.Features.Add("add spoiler");
    }

    public void BuildLuxuryPart()
    {
        this.Car.Features.Add("paint car in gold");
    }

    public Vehicle ReturnResult()
    {
        Vehicle result = this.Car;

        this.Reset();

        return result;
    }

    public void Reset()
    {
        this.Car = new Vehicle();
    }
}