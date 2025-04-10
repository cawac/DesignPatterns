namespace AbstractFactory;

public class ElfRanger: IRanger
{
    public int MaxHealth { get; set; } = 100;
    public int Health { get; set; } = 100;
    public int Damage { get; set; } = 30;
    public int Armor { get; } = 1;
    public void TakeDamage(int damage)
    {
        this.Health -= damage - this.Armor;
    }

    public void Attack(ref ICreature target)
    {
        target.TakeDamage(this.Damage);
    }

    public void RangeAttack(ref ICreature target)
    {
        target.TakeDamage(this.Damage * 3);
    }
}