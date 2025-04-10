namespace Builder;

public class TankBuilder: IBuilder<Tank>
{
    public Tank Car { get; set; }

    public void BuildBasePart()
    {
        this.Car.Features.Add("add tower with gun");
    }

    public void BuildAdditionPart()
    {
        this.Car.Features.Add("add smoke system");
    }

    public void BuildLuxuryPart()
    {
        this.Car.Features.Add("add AI assistant");
    }

    public Tank ReturnResult()
    {
        Tank tank = this.Car;
        
        this.Reset();
        
        return tank;
    }
    
    public void Reset()
    {
        this.Car = new Tank();
    }
}