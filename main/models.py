from django.db import models

class Bottle(models.Model):
    name = models.CharField(max_length=255, verbose_name="Название алкоголя")  # Название алкоголя
    full_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вес полной бутылки в граммах")  # Вес полной бутылки в граммах
    empty_weight = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Вес пустой бутылки в граммах")  # Вес пустой бутылки в граммах
    full_volume = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Объём бутылки в миллилитрах")  # Объём бутылки в миллилитрах
    liquid_density = models.DecimalField(max_digits=10, decimal_places=3, default=0.789, verbose_name="Плотность жидкости (г/мл)") # Плотности жидкости
    image = models.ImageField(upload_to='bottle_images/', null=True, blank=True)  # Поле для изображения

    def __str__(self):
        return self.name

    def calculate_remaining_volume(self, current_weight):
        """
        Рассчитываем оставшийся объём бутылки.
        :param current_weight: Текущий вес бутылки в граммах.
        :return: Оставшийся объём в миллилитрах.
        """
        remaining_weight = current_weight - self.empty_weight
        total_weight = self.full_weight - self.empty_weight
        remaining_volume = (remaining_weight / total_weight) * self.full_volume
        return remaining_volume

    class Meta:
        verbose_name = "Бутылка"
        verbose_name_plural = "Бутылки"