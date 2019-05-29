# Authors: Youness Akourim <akourim97@gmail.com>
# License: BSD 3-Clause

from commpy.modulation import PSKModem, QAMModem

# =============================================================================
# Example constellation plot of Modem
# =============================================================================

# Constellation corresponding to PSKModem for 4 bits per symbols
psk = PSKModem(16)
psk.plotCons()

# Constellation corresponding to QAMModem for 2 bits per symbols
qam = QAMModem(4)
qam.plotCons()
