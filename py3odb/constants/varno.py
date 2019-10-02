"""Constant values for varno names, codes, and descriptions."""


class Varno:
    """Static class for looking up varno information."""
    @staticmethod
    def get_name(code):
        """Get the varno name for the given code."""
        for name, values in VARNO_TABLE.items():
            if values["code"] == code:
                return name
        return "unknown"

    @staticmethod
    def get_code(name):
        """Get the varno code given the name."""
        try:
            return VARNO_TABLE[name]["code"]
        except KeyError:
            return "unknown"

    @staticmethod
    def get_desc(name):
        """Get the description of the given varno."""
        try:
            return VARNO_TABLE[name]["desc"]
        except KeyError:
            return "unknown"


VARNO_TABLE = {
    "1dvar": {
        "desc": "1d-var model level (pseudo)-variable",
        "code": 215
    },
    "aerod": {
        "desc": "aerosol optical depth at 0.55 microns",
        "code": 174
    },
    "airframe_icing": {
        "desc": "airframe icing",
        "code": 227
    },
    "apdss": {
        "desc": "atmospheric path delay in satellite signal",
        "code": 128
    },
    "atmosphere_number": {
        "desc": "SFERICS number of atmospheres",
        "code": 263
    },
    "bend_angle": {
        "desc": "radio occultation bending angle",
        "code": 162
    },
    "binary_snow_cover": {
        "desc": "binary snow cover (0: no snow / 1: presence of snow)",
        "code": 223
    },
    "bt_imaginary": {
        "desc": "brightness temperature imaginary part",
        "code": 191
    },
    "bt_real": {
        "desc": "brightness temperature real part",
        "code": 190
    },
    "c": {
        "desc": "additional cloud group type (c)",
        "code": 69
    },
    "cg_lightning_flash_dens": {
        "desc": "cloud-to-ground lightning flash density ( fl/km2/day)",
        "code": 197
    },
    "ch": {
        "desc": "type of high clouds (ch)",
        "code": 63
    },
    "cl": {
        "desc": "type of low clouds (cl)",
        "code": 65
    },
    "cllqw": {
        "desc": "cloud liquid water",
        "code": 123
    },
    "cloud_cover": {
        "desc": "Total cloud cover",
        "code": 271
    },
    "cloud_frac_clear": {
        "desc": "Cloud clear fraction",
        "code": 247
    },
    "cloud_frac_covered": {
        "desc": "Cloud covered fraction",
        "code": 257
    },
    "cloud_ice_water": {
        "desc": "Cloud ice water",
        "code": 260
    },
    "cloud_radar_reflectivity": {
        "desc": "cloud radar reflectivity",
        "code": 239
    },
    "cloud_top_press": {
        "desc": "Cloud top pressure (Pa)",
        "code": 235
    },
    "cloud_top_temp": {
        "desc": "Cloud top temperature (K)",
        "code": 231
    },
    "cm": {
        "desc": "type of middle clouds (cm)",
        "code": 64
    },
    "cod": {
        "desc": "cloud optical depth",
        "code": 175
    },
    "cpt": {
        "desc": "characteristic of pressure tendency (used in synoptic maps)",
        "code": 130
    },
    "dd": {
        "desc": "wind direction",
        "code": 111
    },
    "depth": {
        "desc": "Depth (m)",
        "code": 272
    },
    "dopp": {
        "desc": "radar doppler wind",
        "code": 195
    },
    "ds": {
        "desc": "ship direction (ds)",
        "code": 83
    },
    "du": {
        "desc": "wind shear (du)",
        "code": 5
    },
    "dv": {
        "desc": "wind shear (dv)",
        "code": 6
    },
    "dwdw": {
        "desc": "wave direction",
        "code": 86
    },
    "dz": {
        "desc": "thickness",
        "code": 57
    },
    "e": {
        "desc": "state of ground (e)",
        "code": 72
    },
    "eses": {
        "desc": "ice thickness (eses)",
        "code": 77
    },
    "ff": {
        "desc": "wind force",
        "code": 112
    },
    "flgt_phase": {
        "desc": "phase of aircraft flight",
        "code": 201
    },
    "gclg": {
        "desc": "general cloud group",
        "code": 87
    },
    "ghg1": {
        "desc": "ghg1: carbon dioxide",
        "code": 186
    },
    "ghg2": {
        "desc": "ghg2: methane",
        "code": 188
    },
    "ghg3": {
        "desc": "ghg3: nitrous oxide",
        "code": 189
    },
    "grg1": {
        "desc": "grg1: no2/nox",
        "code": 181
    },
    "grg2": {
        "desc": "grg2: so2",
        "code": 182
    },
    "grg3": {
        "desc": "grg3: so",
        "code": 183
    },
    "grg4": {
        "desc": "grg4: hcho",
        "code": 184
    },
    "grg5": {
        "desc": "grg5: go3",
        "code": 185
    },
    "height": {
        "desc": "height",
        "code": 156
    },
    "height_assignment_method": {
        "desc": "Height assignment method",
        "code": 211
    },
    "hshs": {
        "desc": "additional cloud group height (hh)",
        "code": 68
    },
    "humidity_mixing_ratio": {
        "desc": "humidity mixing ratio (kg/kg)",
        "code": 226
    },
    "hwhw": {
        "desc": "wave height",
        "code": 84
    },
    "is": {
        "desc": "ice (is)",
        "code": 78
    },
    "jj": {
        "desc": "max. temperature (jj)",
        "code": 81
    },
    "level_cloud": {
        "desc": "Cloud fraction (multi-level)",
        "code": 266
    },
    "level_mixing_ratio": {
        "desc": "humidity_mixing_ratio]",
        "code": 258
    },
    "libksc": {
        "desc": "lidar backscattering",
        "code": 222
    },
    "lidar_aerosol_attenuated_backscatter": {
        "desc": "lidar aerosol attenuated backscatter (1/m*sr)",
        "code": 280
    },
    "lidar_aerosol_extinction": {
        "desc": "lidar aerosol extinction (1/m)",
        "code": 236
    },
    "lidar_cloud_backscatter": {
        "desc": "lidar cloud backscatter",
        "code": 237
    },
    "lidar_cloud_extinction": {
        "desc": "lidar cloud extinction",
        "code": 238
    },
    "lightning": {
        "desc": "Lightning strike observation (ATDNET)",
        "code": 265
    },
    "limb_radiance": {
        "desc": "Limb Radiances",
        "code": 163
    },
    "lnprc": {
        "desc": "log(radar rain rate mm/h + epsilon)",
        "code": 203
    },
    "los": {
        "desc": "horizontal line-of-sight wind component",
        "code": 187
    },
    "lower_layer_p": {
        "desc": "Pressure at bottom of layer SBUV (Pa)",
        "code": 269
    },
    "lwp": {
        "desc": "Liquid water path",
        "code": 244
    },
    "mass_density": {
        "desc": "Mass density",
        "code": 262
    },
    "max_wind_shear1": {
        "desc": "Wind shear above and below 1st maximum wind in sonde profile (s-1)",
        "code": 219
    },
    "max_wind_shear2": {
        "desc": "Wind shear above and below 2nd maximum wind in sonde profile",
        "code": 268
    },
    "mean_freq": {
        "desc": "GPSRO mean frequency",
        "code": 241
    },
    "n": {
        "desc": "total amount of clouds",
        "code": 91
    },
    "nh": {
        "desc": "cloud base height (nh) (meter)",
        "code": 66
    },
    "nn": {
        "desc": "low cloud amount (n)",
        "code": 67
    },
    "ns": {
        "desc": "additional cloud group amount (ns)",
        "code": 70
    },
    "nsoilm": {
        "desc": "normalized soil moisture  (0-100%)",
        "code": 179
    },
    "o3lay": {
        "desc": "layer ozone",
        "code": 206
    },
    "od": {
        "desc": "optical depth",
        "code": 177
    },
    "pmsl": {
        "desc": "Mean sea-level pressure (Pa)",
        "code": 108
    },
    "potential_temp": {
        "desc": "potential temperature (Kelvin)",
        "code": 225
    },
    "prc": {
        "desc": "radar rain rate",
        "code": 202
    },
    "ps": {
        "desc": "surface pressure",
        "code": 110
    },
    "pstandard": {
        "desc": "Standard level pressure (Pa)",
        "code": 109
    },
    "pstation": {
        "desc": "Station pressure (Pa)",
        "code": 107
    },
    "ptend": {
        "desc": "pressure tendency",
        "code": 30
    },
    "pwc": {
        "desc": "precipitable water content",
        "code": 9
    },
    "pwpw": {
        "desc": "wave period",
        "code": 85
    },
    "q": {
        "desc": "specific humidity (q)",
        "code": 7
    },
    "q2m": {
        "desc": "specific humidity at 2m (kg/kg)",
        "code": 281
    },
    "radial_velocity": {
        "desc": "Radial velocity from doppler radar",
        "code": 259
    },
    "ralt_swh": {
        "desc": "significant wave height (m)",
        "code": 220
    },
    "ralt_sws": {
        "desc": "surface wind speed (m/s)",
        "code": 221
    },
    "rao": {
        "desc": "Ratio of fine mode to total aerosol optical depth at 0.55 microns",
        "code": 176
    },
    "rawbt": {
        "desc": "brightness temperature (K)",
        "code": 119
    },
    "rawbt_amsr_89ghz": {
        "desc": "Raw brightness temperature specific to AMSR 89GHz channels (K)",
        "code": 267
    },
    "rawbt_amsu": {
        "desc": "Raw brightness temperature specific to AMSU (K)",
        "code": 249
    },
    "rawbt_clear": {
        "desc": "brightness temperature for clear  (K)",
        "code": 193
    },
    "rawbt_cloudy": {
        "desc": "brightness temperature for cloudy (K)",
        "code": 194
    },
    "rawbt_hirs": {
        "desc": "Raw brightness temperature specific to HIRS (K)",
        "code": 248
    },
    "rawbt_hirs20": {
        "desc": "Raw brightness temperature specific to HIRS (K)",
        "code": 250
    },
    "rawbt_mwhs": {
        "desc": "Raw brightness temperature specific to MWHS (K)",
        "code": 275
    },
    "rawbt_mwts": {
        "desc": "Raw brightness temperature specific to MWTS (K)",
        "code": 274
    },
    "rawra": {
        "desc": "raw radiance",
        "code": 120
    },
    "rawsca": {
        "desc": "Scaled radiance",
        "code": 233
    },
    "refl": {
        "desc": "radar reflectivity",
        "code": 192
    },
    "rfltnc": {
        "desc": "Aerosol reflectance multi-channel",
        "code": 178
    },
    "rh": {
        "desc": "upper air rel. humidity",
        "code": 29
    },
    "rh2m": {
        "desc": "2m rel. humidity",
        "code": 58
    },
    "rhhc": {
        "desc": "rel. humidity from high clouds",
        "code": 90
    },
    "rhlay": {
        "desc": "layer rel. humidity",
        "code": 19
    },
    "rhlc": {
        "desc": "rel. humidity from low clouds",
        "code": 88
    },
    "rhmc": {
        "desc": "rel. humidity from middle clouds",
        "code": 89
    },
    "rr": {
        "desc": "6hr rain (liquid part)",
        "code": 80
    },
    "rs": {
        "desc": "ice code type (rs)",
        "code": 76
    },
    "salinity": {
        "desc": "ocean salinity (PSU)",
        "code": 224
    },
    "satcl": {
        "desc": "cloud amount from satellite",
        "code": 121
    },
    "scatdd": {
        "desc": "ambiguous v component",
        "code": 124
    },
    "scatff": {
        "desc": "ambiguous u component",
        "code": 125
    },
    "scatss": {
        "desc": "sigma 0",
        "code": 122
    },
    "scatwd": {
        "desc": "ambiguous wind direction",
        "code": 126
    },
    "scatws": {
        "desc": "ambiguous wind speed",
        "code": 127
    },
    "sdepth": {
        "desc": "snow depth",
        "code": 71
    },
    "sea_ice": {
        "desc": "Sea ice fraction",
        "code": 253
    },
    "sfall": {
        "desc": "6hr snowfall (solid part of rain)",
        "code": 92
    },
    "soilm": {
        "desc": "soil moisture",
        "code": 180
    },
    "spsp1": {
        "desc": "special phenomena (spsp)#1",
        "code": 74
    },
    "spsp2": {
        "desc": "special phenomena (spsp)#2",
        "code": 75
    },
    "ssh": {
        "desc": "Sea surface height (m)",
        "code": 273
    },
    "t": {
        "desc": "upper air temperature (K)",
        "code": 2
    },
    "t2m": {
        "desc": "2m temperature (K)",
        "code": 39
    },
    "tcwv": {
        "desc": "Total column water vapour",
        "code": 245
    },
    "td": {
        "desc": "upper air dew point (K)",
        "code": 59
    },
    "td2m": {
        "desc": "2m dew point (K)",
        "code": 40
    },
    "tgtg": {
        "desc": "ground temperature (tgtg)",
        "code": 73
    },
    "tot_lightning_flash_dens": {
        "desc": "total (cloud-to-ground plus intra-cloud) lightning flash density (fl/km2/day)",
        "code": 196
    },
    "tot_zen_delay": {
        "desc": "Total zenith delay (GPS)",
        "code": 229
    },
    "tot_zen_delay_err": {
        "desc": "Total zenith delay error (GPS)",
        "code": 230
    },
    "trtr": {
        "desc": "original time period of rain obs. (trtr)",
        "code": 79
    },
    "ts": {
        "desc": "surface temperature (K)",
        "code": 11
    },
    "tsts": {
        "desc": "sea water temperature (used in synoptic maps)",
        "code": 12
    },
    "turbulence_index": {
        "desc": "turbulence index",
        "code": 228
    },
    "u": {
        "desc": "upper air u component",
        "code": 3
    },
    "u10m": {
        "desc": "10m u component (m/s)",
        "code": 41
    },
    "u_amb": {
        "desc": "Ambiguous u-wind component (m/s)",
        "code": 242
    },
    "upper_layer_p": {
        "desc": "Pressure at top of later SBUV (Pa)",
        "code": 270
    },
    "v": {
        "desc": "upper air v component",
        "code": 4
    },
    "v10m": {
        "desc": "10m v component (m/s)",
        "code": 42
    },
    "v_amb": {
        "desc": "Ambiguous v-wind component (m/s)",
        "code": 243
    },
    "vert_vv": {
        "desc": "Vertical visibility (m)",
        "code": 218
    },
    "vs": {
        "desc": "ship speed (vs)",
        "code": 82
    },
    "vsp": {
        "desc": "vertical speed",
        "code": 8
    },
    "vt": {
        "desc": "virtual temperature",
        "code": 56
    },
    "vv": {
        "desc": "visibility",
        "code": 62
    },
    "w": {
        "desc": "past weather (w)",
        "code": 60
    },
    "w2": {
        "desc": "past weather 2 (used in synoptic maps)",
        "code": 160
    },
    "wind_gust": {
        "desc": "Maximum wind gust (m/s)",
        "code": 261
    },
    "ww": {
        "desc": "present weather (ww)",
        "code": 61
    },
    "z": {
        "desc": "geopotential",
        "code": 1
    }
}
