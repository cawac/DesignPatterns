namespace AbstractFactory;

public interface IRanger: ICreature
{
    void RangeAttack(ref ICreature target);
}