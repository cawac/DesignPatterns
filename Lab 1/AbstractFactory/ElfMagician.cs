namespace AbstractFactory;

public class ElfMagician: IMagician
{
    public int MaxHealth { get; set; } = 50;
    public int Health { get; set; } = 50;
    public int Damage { get; set; } = 30;
    public int Armor { get; } = 0;
    public void TakeDamage(int damage)
    {
        Health -= damage - this.Armor;
    }

    public void Attack(ref ICreature target)
    {
        target.TakeDamage(this.Damage);
    }

    public void Heal(ref ICreature target)
    {
        target.Health = target.Health + this.Damage > target.MaxHealth ? target.MaxHealth : target.Health + this.Damage;
    }
}