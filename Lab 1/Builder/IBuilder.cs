namespace Builder;

public interface IBuilder<out TCar>
{
    public TCar? GetResult();
        
    public void Reset();
}