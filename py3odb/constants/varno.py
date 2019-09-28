"""Constant values for varno codes."""


class Varno:
    """Static class for looking up varno codes."""
    @staticmethod
    def get_code(varno):
        """Get the alphanumeric code corresponding to the given varno."""
        for code, values in VARNO_CODES.items():
            if values["varno"] == varno:
                return code
        return "unknown"

    @staticmethod
    def get_varno(code):
        """Get the varno given the corresponding alphanumeric code."""
        try:
            return VARNO_CODES[code]["varno"]
        except KeyError:
            return "unknown"

    @staticmethod
    def get_desc(code):
        """Get the description of the given varno."""
        try:
            return VARNO_CODES[code]["desc"]
        except KeyError:
            return "unknown"


VARNO_CODES = {
    "1dvar": {
        "desc": "1d-var model level (pseudo)-variable",
        "varno": 215
    },
    "aerod": {
        "desc": "aerosol optical depth at 0.55 microns",
        "varno": 174
    },
    "airframe_icing": {
        "desc": "airframe icing",
        "varno": 227
    },
    "apdss": {
        "desc": "atmospheric path delay in satellite signal",
        "varno": 128
    },
    "atmosphere_number": {
        "desc": "SFERICS number of atmospheres",
        "varno": 263
    },
    "bend_angle": {
        "desc": "radio occultation bending angle",
        "varno": 162
    },
    "binary_snow_cover": {
        "desc": "binary snow cover (0: no snow / 1: presence of snow)",
        "varno": 223
    },
    "bt_imaginary": {
        "desc": "brightness temperature imaginary part",
        "varno": 191
    },
    "bt_real": {
        "desc": "brightness temperature real part",
        "varno": 190
    },
    "c": {
        "desc": "additional cloud group type (c)",
        "varno": 69
    },
    "cg_lightning_flash_dens": {
        "desc": "cloud-to-ground lightning flash density ( fl/km2/day)",
        "varno": 197
    },
    "ch": {
        "desc": "type of high clouds (ch)",
        "varno": 63
    },
    "cl": {
        "desc": "type of low clouds (cl)",
        "varno": 65
    },
    "cllqw": {
        "desc": "cloud liquid water",
        "varno": 123
    },
    "cloud_cover": {
        "desc": "Total cloud cover",
        "varno": 271
    },
    "cloud_frac_clear": {
        "desc": "Cloud clear fraction",
        "varno": 247
    },
    "cloud_frac_covered": {
        "desc": "Cloud covered fraction",
        "varno": 257
    },
    "cloud_ice_water": {
        "desc": "Cloud ice water",
        "varno": 260
    },
    "cloud_radar_reflectivity": {
        "desc": "cloud radar reflectivity",
        "varno": 239
    },
    "cloud_top_press": {
        "desc": "Cloud top pressure (Pa)",
        "varno": 235
    },
    "cloud_top_temp": {
        "desc": "Cloud top temperature (K)",
        "varno": 231
    },
    "cm": {
        "desc": "type of middle clouds (cm)",
        "varno": 64
    },
    "cod": {
        "desc": "cloud optical depth",
        "varno": 175
    },
    "cpt": {
        "desc": "characteristic of pressure tendency (used in synoptic maps)",
        "varno": 130
    },
    "dd": {
        "desc": "wind direction",
        "varno": 111
    },
    "depth": {
        "desc": "Depth (m)",
        "varno": 272
    },
    "dopp": {
        "desc": "radar doppler wind",
        "varno": 195
    },
    "ds": {
        "desc": "ship direction (ds)",
        "varno": 83
    },
    "du": {
        "desc": "wind shear (du)",
        "varno": 5
    },
    "dv": {
        "desc": "wind shear (dv)",
        "varno": 6
    },
    "dwdw": {
        "desc": "wave direction",
        "varno": 86
    },
    "dz": {
        "desc": "thickness",
        "varno": 57
    },
    "e": {
        "desc": "state of ground (e)",
        "varno": 72
    },
    "eses": {
        "desc": "ice thickness (eses)",
        "varno": 77
    },
    "ff": {
        "desc": "wind force",
        "varno": 112
    },
    "flgt_phase": {
        "desc": "phase of aircraft flight",
        "varno": 201
    },
    "gclg": {
        "desc": "general cloud group",
        "varno": 87
    },
    "ghg1": {
        "desc": "ghg1: carbon dioxide",
        "varno": 186
    },
    "ghg2": {
        "desc": "ghg2: methane",
        "varno": 188
    },
    "ghg3": {
        "desc": "ghg3: nitrous oxide",
        "varno": 189
    },
    "grg1": {
        "desc": "grg1: no2/nox",
        "varno": 181
    },
    "grg2": {
        "desc": "grg2: so2",
        "varno": 182
    },
    "grg3": {
        "desc": "grg3: so",
        "varno": 183
    },
    "grg4": {
        "desc": "grg4: hcho",
        "varno": 184
    },
    "grg5": {
        "desc": "grg5: go3",
        "varno": 185
    },
    "height": {
        "desc": "height",
        "varno": 156
    },
    "height_assignment_method": {
        "desc": "Height assignment method",
        "varno": 211
    },
    "hshs": {
        "desc": "additional cloud group height (hh)",
        "varno": 68
    },
    "humidity_mixing_ratio": {
        "desc": "humidity mixing ratio (kg/kg)",
        "varno": 226
    },
    "hwhw": {
        "desc": "wave height",
        "varno": 84
    },
    "is": {
        "desc": "ice (is)",
        "varno": 78
    },
    "jj": {
        "desc": "max. temperature (jj)",
        "varno": 81
    },
    "level_cloud": {
        "desc": "Cloud fraction (multi-level)",
        "varno": 266
    },
    "level_mixing_ratio": {
        "desc": "humidity_mixing_ratio]",
        "varno": 258
    },
    "libksc": {
        "desc": "lidar backscattering",
        "varno": 222
    },
    "lidar_aerosol_attenuated_backscatter": {
        "desc": "lidar aerosol attenuated backscatter (1/m*sr)",
        "varno": 280
    },
    "lidar_aerosol_extinction": {
        "desc": "lidar aerosol extinction (1/m)",
        "varno": 236
    },
    "lidar_cloud_backscatter": {
        "desc": "lidar cloud backscatter",
        "varno": 237
    },
    "lidar_cloud_extinction": {
        "desc": "lidar cloud extinction",
        "varno": 238
    },
    "lightning": {
        "desc": "Lightning strike observation (ATDNET)",
        "varno": 265
    },
    "limb_radiance": {
        "desc": "Limb Radiances",
        "varno": 163
    },
    "lnprc": {
        "desc": "log(radar rain rate mm/h + epsilon)",
        "varno": 203
    },
    "los": {
        "desc": "horizontal line-of-sight wind component",
        "varno": 187
    },
    "lower_layer_p": {
        "desc": "Pressure at bottom of layer SBUV (Pa)",
        "varno": 269
    },
    "lwp": {
        "desc": "Liquid water path",
        "varno": 244
    },
    "mass_density": {
        "desc": "Mass density",
        "varno": 262
    },
    "max_wind_shear1": {
        "desc": "Wind shear above and below 1st maximum wind in sonde profile (s-1)",
        "varno": 219
    },
    "max_wind_shear2": {
        "desc": "Wind shear above and below 2nd maximum wind in sonde profile",
        "varno": 268
    },
    "mean_freq": {
        "desc": "GPSRO mean frequency",
        "varno": 241
    },
    "n": {
        "desc": "total amount of clouds",
        "varno": 91
    },
    "nh": {
        "desc": "cloud base height (nh) (meter)",
        "varno": 66
    },
    "nn": {
        "desc": "low cloud amount (n)",
        "varno": 67
    },
    "ns": {
        "desc": "additional cloud group amount (ns)",
        "varno": 70
    },
    "nsoilm": {
        "desc": "normalized soil moisture  (0-100%)",
        "varno": 179
    },
    "o3lay": {
        "desc": "layer ozone",
        "varno": 206
    },
    "od": {
        "desc": "optical depth",
        "varno": 177
    },
    "pmsl": {
        "desc": "Mean sea-level pressure (Pa)",
        "varno": 108
    },
    "potential_temp": {
        "desc": "potential temperature (Kelvin)",
        "varno": 225
    },
    "prc": {
        "desc": "radar rain rate",
        "varno": 202
    },
    "ps": {
        "desc": "surface pressure",
        "varno": 110
    },
    "pstandard": {
        "desc": "Standard level pressure (Pa)",
        "varno": 109
    },
    "pstation": {
        "desc": "Station pressure (Pa)",
        "varno": 107
    },
    "ptend": {
        "desc": "pressure tendency",
        "varno": 30
    },
    "pwc": {
        "desc": "precipitable water content",
        "varno": 9
    },
    "pwpw": {
        "desc": "wave period",
        "varno": 85
    },
    "q": {
        "desc": "specific humidity (q)",
        "varno": 7
    },
    "q2m": {
        "desc": "specific humidity at 2m (kg/kg)",
        "varno": 281
    },
    "radial_velocity": {
        "desc": "Radial velocity from doppler radar",
        "varno": 259
    },
    "ralt_swh": {
        "desc": "significant wave height (m)",
        "varno": 220
    },
    "ralt_sws": {
        "desc": "surface wind speed (m/s)",
        "varno": 221
    },
    "rao": {
        "desc": "Ratio of fine mode to total aerosol optical depth at 0.55 microns",
        "varno": 176
    },
    "rawbt": {
        "desc": "brightness temperature (K)",
        "varno": 119
    },
    "rawbt_amsr_89ghz": {
        "desc": "Raw brightness temperature specific to AMSR 89GHz channels (K)",
        "varno": 267
    },
    "rawbt_amsu": {
        "desc": "Raw brightness temperature specific to AMSU (K)",
        "varno": 249
    },
    "rawbt_clear": {
        "desc": "brightness temperature for clear  (K)",
        "varno": 193
    },
    "rawbt_cloudy": {
        "desc": "brightness temperature for cloudy (K)",
        "varno": 194
    },
    "rawbt_hirs": {
        "desc": "Raw brightness temperature specific to HIRS (K)",
        "varno": 248
    },
    "rawbt_hirs20": {
        "desc": "Raw brightness temperature specific to HIRS (K)",
        "varno": 250
    },
    "rawbt_mwhs": {
        "desc": "Raw brightness temperature specific to MWHS (K)",
        "varno": 275
    },
    "rawbt_mwts": {
        "desc": "Raw brightness temperature specific to MWTS (K)",
        "varno": 274
    },
    "rawra": {
        "desc": "raw radiance",
        "varno": 120
    },
    "rawsca": {
        "desc": "Scaled radiance",
        "varno": 233
    },
    "refl": {
        "desc": "radar reflectivity",
        "varno": 192
    },
    "rfltnc": {
        "desc": "Aerosol reflectance multi-channel",
        "varno": 178
    },
    "rh": {
        "desc": "upper air rel. humidity",
        "varno": 29
    },
    "rh2m": {
        "desc": "2m rel. humidity",
        "varno": 58
    },
    "rhhc": {
        "desc": "rel. humidity from high clouds",
        "varno": 90
    },
    "rhlay": {
        "desc": "layer rel. humidity",
        "varno": 19
    },
    "rhlc": {
        "desc": "rel. humidity from low clouds",
        "varno": 88
    },
    "rhmc": {
        "desc": "rel. humidity from middle clouds",
        "varno": 89
    },
    "rr": {
        "desc": "6hr rain (liquid part)",
        "varno": 80
    },
    "rs": {
        "desc": "ice code type (rs)",
        "varno": 76
    },
    "salinity": {
        "desc": "ocean salinity (PSU)",
        "varno": 224
    },
    "satcl": {
        "desc": "cloud amount from satellite",
        "varno": 121
    },
    "scatdd": {
        "desc": "ambiguous v component",
        "varno": 124
    },
    "scatff": {
        "desc": "ambiguous u component",
        "varno": 125
    },
    "scatss": {
        "desc": "sigma 0",
        "varno": 122
    },
    "scatwd": {
        "desc": "ambiguous wind direction",
        "varno": 126
    },
    "scatws": {
        "desc": "ambiguous wind speed",
        "varno": 127
    },
    "sdepth": {
        "desc": "snow depth",
        "varno": 71
    },
    "sea_ice": {
        "desc": "Sea ice fraction",
        "varno": 253
    },
    "sfall": {
        "desc": "6hr snowfall (solid part of rain)",
        "varno": 92
    },
    "soilm": {
        "desc": "soil moisture",
        "varno": 180
    },
    "spsp1": {
        "desc": "special phenomena (spsp)#1",
        "varno": 74
    },
    "spsp2": {
        "desc": "special phenomena (spsp)#2",
        "varno": 75
    },
    "ssh": {
        "desc": "Sea surface height (m)",
        "varno": 273
    },
    "t": {
        "desc": "upper air temperature (K)",
        "varno": 2
    },
    "t2m": {
        "desc": "2m temperature (K)",
        "varno": 39
    },
    "tcwv": {
        "desc": "Total column water vapour",
        "varno": 245
    },
    "td": {
        "desc": "upper air dew point (K)",
        "varno": 59
    },
    "td2m": {
        "desc": "2m dew point (K)",
        "varno": 40
    },
    "tgtg": {
        "desc": "ground temperature (tgtg)",
        "varno": 73
    },
    "tot_lightning_flash_dens": {
        "desc": "total (cloud-to-ground plus intra-cloud) lightning flash density (fl/km2/day)",
        "varno": 196
    },
    "tot_zen_delay": {
        "desc": "Total zenith delay (GPS)",
        "varno": 229
    },
    "tot_zen_delay_err": {
        "desc": "Total zenith delay error (GPS)",
        "varno": 230
    },
    "trtr": {
        "desc": "original time period of rain obs. (trtr)",
        "varno": 79
    },
    "ts": {
        "desc": "surface temperature (K)",
        "varno": 11
    },
    "tsts": {
        "desc": "sea water temperature (used in synoptic maps)",
        "varno": 12
    },
    "turbulence_index": {
        "desc": "turbulence index",
        "varno": 228
    },
    "u": {
        "desc": "upper air u component",
        "varno": 3
    },
    "u10m": {
        "desc": "10m u component (m/s)",
        "varno": 41
    },
    "u_amb": {
        "desc": "Ambiguous u-wind component (m/s)",
        "varno": 242
    },
    "upper_layer_p": {
        "desc": "Pressure at top of later SBUV (Pa)",
        "varno": 270
    },
    "v": {
        "desc": "upper air v component",
        "varno": 4
    },
    "v10m": {
        "desc": "10m v component (m/s)",
        "varno": 42
    },
    "v_amb": {
        "desc": "Ambiguous v-wind component (m/s)",
        "varno": 243
    },
    "vert_vv": {
        "desc": "Vertical visibility (m)",
        "varno": 218
    },
    "vs": {
        "desc": "ship speed (vs)",
        "varno": 82
    },
    "vsp": {
        "desc": "vertical speed",
        "varno": 8
    },
    "vt": {
        "desc": "virtual temperature",
        "varno": 56
    },
    "vv": {
        "desc": "visibility",
        "varno": 62
    },
    "w": {
        "desc": "past weather (w)",
        "varno": 60
    },
    "w2": {
        "desc": "past weather 2 (used in synoptic maps)",
        "varno": 160
    },
    "wind_gust": {
        "desc": "Maximum wind gust (m/s)",
        "varno": 261
    },
    "ww": {
        "desc": "present weather (ww)",
        "varno": 61
    },
    "z": {
        "desc": "geopotential",
        "varno": 1
    }
}
