namespace Builder;

public interface IBuilder<out TCar>
{
    public void BuildBase(string Name, double weight, double length, double maxSpeed);
    
    public TCar? GetResult();
    
    public void Reset();
}