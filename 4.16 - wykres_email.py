import matplotlib.pyplot as plt

email = "radoslaw.janiak@rajkonkret.pl"

plt.text(0.5, 0.5, email, ha="center", va='center', fontsize=24)
plt.axis('off')

plt.savefig("wykres_email.pdf", format='pdf')
plt.show()
