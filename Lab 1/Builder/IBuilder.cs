namespace Builder;

public interface IBuilder
{
    void BuildBasePart();
    
    void BuildAdditionPart();
    
    void BuildLuxuryPart();
    
    void Reset();
}

public interface IBuilder<T>: IBuilder
{
    public T Car { get; set; }

    T ReturnResult();
}