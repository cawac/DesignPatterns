namespace Builder;

public class CargoBuilder: IBuilder<Cargo>
{
    public Cargo Car { get; set; }

    public void BuildBasePart()
    {
        this.Car.Features.Add("add doors");
    }

    public void BuildAdditionPart()
    {
        this.Car.Features.Add("add navigator");
        this.Car.Features.Add("add cruise control");
    }

    public void BuildLuxuryPart()
    {
        this.Car.Features.Add("add autopilot");
    }

    public Cargo ReturnResult()
    {
        Cargo result = this.Car;
        
        this.Reset();

        return result;
    }

    public void Reset()
    {
        this.Car = new Cargo();
    }
}